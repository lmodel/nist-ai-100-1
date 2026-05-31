package None;

/* metamodel_version: 1.11.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  An engineered or machine-based system that can, for a given set
of objectives, generate outputs such as predictions,
recommendations, or decisions influencing real or virtual
environments. AI systems are designed to operate with varying
levels of autonomy (Adapted from OECD Recommendation on AI:2019;
ISO/IEC 22989:2022).
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiSystem extends NamedThingRMF {

  private List<String> lifecycleStage;
  private List<String> aiDimension;


}