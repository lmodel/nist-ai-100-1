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
  A socio-technical dimension of an AI system (Figure 2):
Application Context, Data and Input, AI Model, Task and Output,
or People and Planet.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiSystemDimension extends NamedThingRMF {

  private String dimensionKind;


}