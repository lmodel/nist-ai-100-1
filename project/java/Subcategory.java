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
  A subcategory within an AI RMF Core category (e.g., "GOVERN 1.1:
Legal and regulatory requirements involving AI are understood,
managed, and documented"). Subcategories express specific
outcomes.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class Subcategory extends NamedThingRMF {

  private String subcategoryId;
  private String outcome;
  private List<String> trustworthinessCharacteristic;
  private List<String> lifecycleStage;
  private String aboutText;
  private String suggestedActionsText;
  private String documentationQuestions;
  private String referencesText;
  private List<String> topics;
  private List<String> aiActorCategories;


}